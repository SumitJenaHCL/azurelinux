#!/bin/bash

echo "executing liveos-artifacts-download.sh" > /dev/kmsg

. /usr/lib/dracut-lib.sh
root=$(getarg root -d "")

downloadedArtifactsDirs=/run/initramfs/downloaded-artifacts

set -e

function isSupportedProtocol() {
    local kernelParamValue=$1

    case "$kernelParamValue" in
        live:http://* | http://*)
            # remove `live:` if it exists
            urlValue="${kernelParamValue#live:}"
            ;;
    esac

    echo $urlValue
}

function downloadArtifact () {
    local paramValueNoLive=$1

    IFS=';'
    read -ra valueParts <<< "$paramValueNoLive"
    IFS=$' \t\n'

    sourceUrl=${valueParts[0]}
    targetDir=
    targetPath=
    arrayLength=${#valueParts[@]}
    if (( arrayLength > 1 )); then
        targetPath=${valueParts[1]}
    else
        targetPath=$downloadedArtifactsDirs/${sourceUrl##*/}
    fi
    targetDir="${targetPath%/*}"

    mkdir -p $targetDir
    httpRetCode=$(curl $sourceUrl -o $targetPath -w "%{http_code}\n")
    # echo "curl returned ($httpRetCode)" > /dev/kmsg
    if [ $httpRetCode -ne 200 ]; then
        echo "error: failed to download $sourceUrl" > /dev/kmsg
        exit 0
    fi

    echo $targetPath
}

# download
isoUrl=$(isSupportedProtocol "$root")
if [[ -z "$isoUrl" ]]; then
    # this is not a live iso url, there is nothing for us to do.
    echo "root is set to a non-live iso url ($root)" > /dev/kmsg
    exit 0
fi
localIsoPath=$(downloadArtifact "$isoUrl")
if [[ "$localIsoPath" == "error:"* ]]; then
    echo "failed to download ($isoUrl)" > /dev/kmsg
    exit 1
fi

# create a loopback device and prepare rootfs
rootDevice=$(losetup -f --show $localIsoPath)

# set dracut environment
export fstype="auto"
export DRACUT_SYSTEMD=1

# let dmsquash-live-root handle the mounting as before
/usr/sbin/dmsquash-live-root $rootDevice
