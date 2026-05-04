# ZDI-23-1769: Microsoft Skype Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1769
- **ZDI-CAN:** ZDI-CAN-19099
- **Date:** 2023-12-13
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Skype
- **Credit:** Hector Peralta (@hperalta89) and Nicolas Armua (https://www.linkedin.com/in/slyfer/)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1769/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Skype. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of visited URLs. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-us/acknowledgement/online

## Disclosure Timeline

- 2022-10-20 - Vulnerability reported to vendor
- 2023-12-13 - Coordinated public release of advisory
