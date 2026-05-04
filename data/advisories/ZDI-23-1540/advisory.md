# ZDI-23-1540: (Pwn2Own) Microsoft Teams Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1540
- **ZDI-CAN:** ZDI-CAN-20720
- **Date:** 2023-10-11
- **CVE:** N/A
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** vcslab of Team Viettel (@vcslab)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1540/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Teams. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the description parameter within a bot app manifest file. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2023-04-05 - Vulnerability reported to vendor
- 2023-10-11 - Coordinated public release of advisory
