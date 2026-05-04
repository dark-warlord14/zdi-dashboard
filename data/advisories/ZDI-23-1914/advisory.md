# ZDI-23-1914: Google Chromium JIT Compilation Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1914
- **ZDI-CAN:** ZDI-CAN-21536
- **Date:** 2024-06-06
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Google
- **Affected Products:** Chromium
- **Credit:** Hossein Lotfi of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1914/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Google Chromium. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within JIT compilation. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromium.googlesource.com/v8/v8/+/7effdbf988a7d18f4cbe9dece94929ff76eae600

## Disclosure Timeline

- 2023-06-30 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
