# ZDI-21-1003: TeamViewer TVS File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1003
- **ZDI-CAN:** ZDI-CAN-13697
- **Date:** 2021-08-26
- **CVE:** CVE-2021-34859
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** TeamViewer
- **Affected Products:** TeamViewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1003/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of TeamViewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TVS files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

TeamViewer has issued an update to correct this vulnerability. More details can be found at: https://community.teamviewer.com/English/discussion/117794/august-updates-security-patches/p1

## Disclosure Timeline

- 2021-04-27 - Vulnerability reported to vendor
- 2021-08-26 - Coordinated public release of advisory
