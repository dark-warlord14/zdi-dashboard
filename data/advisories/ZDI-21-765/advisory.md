# ZDI-21-765: Apple macOS AudioToolboxCore RF64 File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-765
- **ZDI-CAN:** ZDI-CAN-12838
- **Date:** 2021-06-25
- **CVE:** CVE-2021-30707
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** hjy79425575
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-765/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the AudioToolboxCore library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the parsing of RF64 audio files. A crafted RF64 file can trigger an overflow of a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212529

## Disclosure Timeline

- 2021-02-25 - Vulnerability reported to vendor
- 2021-06-25 - Coordinated public release of advisory
