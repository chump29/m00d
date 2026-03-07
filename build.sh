#!/usr/bin/env -S bash -e

for img in backend frontend; do
    pushd $img > /dev/null || exit
    ./build.sh
    popd > /dev/null || exit
done
