# ZDI-24-1422: Nikon NEF Codec Thumbnail Provider NRW File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1422
- **ZDI-CAN:** ZDI-CAN-19873
- **Date:** 2024-10-24
- **CVE:** CVE-2024-8025
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Nikon
- **Affected Products:** NEF Codec
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1422/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Nikon NEF Codec. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of NRW files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Nikon has issued an update to correct this vulnerability. More details can be found at: https://downloadcenter.nikonimglib.com/en/download/sw/259.html

## Disclosure Timeline

- 2024-06-27 - Vulnerability reported to vendor
- 2024-10-24 - Coordinated public release of advisory
- 2024-10-24 - Advisory Updated
