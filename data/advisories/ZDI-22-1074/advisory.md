# ZDI-22-1074: Microsoft Outlook MIME Header Heap Corruption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1074
- **ZDI-CAN:** ZDI-CAN-17384
- **Date:** 2022-08-18
- **CVE:** CVE-2022-35742
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Outlook
- **Credit:** insu of 78 Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1074/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Outlook. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of MIME headers. Crafted MIME headers within an email message can cause Outlook to release an invalid pointer. An attacker can leverage this vulnerability to create a persistent denial-of-service condition on the Microsoft Outlook application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35742

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory
