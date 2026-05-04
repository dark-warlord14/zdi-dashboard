# ZDI-22-082: TeamViewer Improper Validation of Array Index Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-082
- **ZDI-CAN:** ZDI-CAN-13818
- **Date:** 2022-01-20
- **CVE:** CVE-2021-35005
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** TeamViewer
- **Affected Products:** TeamViewer
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-082/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of TeamViewer. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the TeamViewer service. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated array. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

TeamViewer has issued an update to correct this vulnerability. More details can be found at: https://community.teamviewer.com/English/discussion/117794/august-updates-security-patches

## Disclosure Timeline

- 2021-06-18 - Vulnerability reported to vendor
- 2022-01-20 - Coordinated public release of advisory
