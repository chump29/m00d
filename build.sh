#!/usr/bin/env -S bash -e

for img in backend frontend; do
    pushd $img > /dev/null || exit 1
    ./build.sh
    popd > /dev/null || exit 1
done
