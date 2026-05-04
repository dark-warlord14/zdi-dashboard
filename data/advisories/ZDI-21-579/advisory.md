# ZDI-21-579: Microsoft Windows Groove Music FLAC File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-579
- **ZDI-CAN:** ZDI-CAN-13237
- **Date:** 2021-05-13
- **CVE:** CVE-2021-28465
- **CVSS:** 6.6
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** garmin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-579/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of FLAC files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current user at low integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-28465

## Disclosure Timeline

- 2021-03-10 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
