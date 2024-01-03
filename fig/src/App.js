import * as React from "react";

function MyComponent(props) {
  return (
    <div className="bg-white flex flex-col items-stretch pt-6 pb-12 px-20 max-md:px-5">
      <div className="justify-between items-stretch flex w-full gap-5 px-8 py-2.5 max-md:max-w-full max-md:flex-wrap max-md:px-5">
        <div className="items-stretch self-center flex gap-3 my-auto">
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/f466301822a0123570d734f3426582db3ce0c4a1b0ec60a9a706683165bdfdcc?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&"
            className="aspect-square object-contain object-center w-10 overflow-hidden shrink-0 max-w-full"
          />
          <div className="text-black text-xl font-bold leading-6 tracking-tight capitalize self-center my-auto">
            DP
          </div>
        </div>
        <div className="justify-between items-stretch self-center flex gap-5 my-auto max-md:max-w-full max-md:flex-wrap">
          <div className="text-black text-xl font-semibold leading-6 tracking-tight capitalize grow whitespace-nowrap">
            About Me
          </div>
          <div className="text-black text-xl font-semibold leading-6 tracking-tight capitalize">
            Skills
          </div>
          <div className="text-black text-xl font-semibold leading-6 tracking-tight capitalize">
            Project
          </div>
          <div className="text-black text-xl font-semibold leading-6 tracking-tight capitalize grow whitespace-nowrap">
            Contact me
          </div>
        </div>
        <div className="justify-between items-stretch rounded bg-black flex gap-2 px-5 py-4">
          <div className="text-white text-xl font-semibold leading-6 tracking-wide grow whitespace-nowrap">
            Resume
          </div>
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/d68e0b508cb674652e50eeb888851b903292815d4d698a7ced624352c317d75a?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&"
            className="aspect-square object-contain object-center w-5 overflow-hidden self-center shrink-0 max-w-full my-auto"
          />
        </div>
      </div>
      <div className="self-center w-full max-w-[1551px] mt-48 mb-24 max-md:max-w-full max-md:my-10">
        <div className="gap-5 flex max-md:flex-col max-md:items-stretch max-md:gap-0">
          <div className="flex flex-col items-stretch w-[48%] max-md:w-full max-md:ml-0">
            <div className="z-[1] flex flex-col items-stretch mt-14 max-md:max-w-full max-md:mt-10">
              <div className="items-stretch flex justify-between gap-4 max-md:max-w-full max-md:flex-wrap">
                <div className="text-black text-5xl leading-[56.16px] tracking-tighter grow shrink basis-auto max-md:text-4xl">
                  Hello I’am
                </div>
                <div className="text-black text-5xl font-extrabold leading-[56.16px] tracking-tighter grow shrink basis-auto max-md:max-w-full max-md:text-4xl">
                  Dinakar Pathakota
                </div>
              </div>
              <div className="items-stretch flex gap-4 mt-5 self-start">
                <div className="text-black text-5xl font-extrabold leading-[56.16px] tracking-tighter grow whitespace-nowrap max-md:text-4xl">
                  CSE
                </div>
                <div className="text-5xl font-extrabold leading-[56.16px] tracking-tighter max-md:text-4xl">
                  Student
                </div>
              </div>
              <div className="items-stretch flex justify-between gap-4 mt-5 max-md:max-w-full max-md:flex-wrap">
                <div className="text-black text-5xl leading-[56.16px] tracking-tighter grow shrink basis-auto max-md:text-4xl">
                  Based In
                </div>
                <div className="text-black text-5xl font-extrabold leading-[56.16px] tracking-tighter grow shrink basis-auto max-md:max-w-full max-md:text-4xl">
                  Hyderabad.
                </div>
              </div>
              <div className="flex w-[365px] max-w-full items-stretch justify-between gap-5 mt-9 self-start">
                <div className="justify-center items-center rounded bg-white flex aspect-[1.037037037037037] flex-col h-[55px] flex-1 px-2">
                  <img
                    loading="lazy"
                    srcSet="https://cdn.builder.io/api/v1/image/assets/TEMP/d05c3d598ccdcfa3aa477afb2b2dc7d3082d1f5970b35f80e5952babba394b6a?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&width=100 100w, https://cdn.builder.io/api/v1/image/assets/TEMP/d05c3d598ccdcfa3aa477afb2b2dc7d3082d1f5970b35f80e5952babba394b6a?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&width=200 200w, https://cdn.builder.io/api/v1/image/assets/TEMP/d05c3d598ccdcfa3aa477afb2b2dc7d3082d1f5970b35f80e5952babba394b6a?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&width=400 400w, https://cdn.builder.io/api/v1/image/assets/TEMP/d05c3d598ccdcfa3aa477afb2b2dc7d3082d1f5970b35f80e5952babba394b6a?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&width=800 800w, https://cdn.builder.io/api/v1/image/assets/TEMP/d05c3d598ccdcfa3aa477afb2b2dc7d3082d1f5970b35f80e5952babba394b6a?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&width=1200 1200w, https://cdn.builder.io/api/v1/image/assets/TEMP/d05c3d598ccdcfa3aa477afb2b2dc7d3082d1f5970b35f80e5952babba394b6a?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&width=1600 1600w, https://cdn.builder.io/api/v1/image/assets/TEMP/d05c3d598ccdcfa3aa477afb2b2dc7d3082d1f5970b35f80e5952babba394b6a?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&width=2000 2000w, https://cdn.builder.io/api/v1/image/assets/TEMP/d05c3d598ccdcfa3aa477afb2b2dc7d3082d1f5970b35f80e5952babba394b6a?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&"
                    className="aspect-[1.03] object-contain object-center w-full overflow-hidden"
                  />
                </div>
                <div className="justify-center items-center rounded bg-black flex shrink-0 h-[54px] flex-col flex-1" />
                <div className="justify-center items-center rounded bg-black flex shrink-0 h-[54px] flex-col flex-1" />
                <div className="justify-center items-center rounded bg-black flex shrink-0 h-[54px] flex-col flex-1" />
              </div>
            </div>
          </div>
          <div className="flex flex-col items-stretch w-[52%] ml-5 max-md:w-full max-md:ml-0">
            <img
              loading="lazy"
              src="https://cdn.builder.io/api/v1/image/assets/TEMP/dad380aa36f03d9b0793eb4601dec3cd38179d86b15894520c617fea3d1bb93d?apiKey=3a87cd0d2ccb4bbfb5ec29fcb9c9122c&"
              className="aspect-[1.49] object-contain object-center w-full justify-end items-center overflow-hidden grow max-md:max-w-full"
            />
          </div>
        </div>
      </div>
    </div>
  );
}


