# ZDI-24-1097: (0Day) Microsoft GitHub Dev-Containers Improper Privilege Management Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1097
- **ZDI-CAN:** ZDI-CAN-22453
- **Date:** 2024-08-06
- **CVE:** N/A
- **CVSS:** 9.9
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** GitHub
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1097/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on Microsoft GitHub. Authentication is required to exploit this vulnerability. The specific flaw exists within the configuration of Dev-Containers. The application does not enforce the privileged flag within a devcontainer configuration. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the host.

## Additional Details

11/03/23 – ZDI reported the vulnerability to the vendor. 11/03/23 – Github states this case needs to be handled directly with Microsoft. 11/06/23 – ZDI resent the case to Microsoft. 11/22/23 – The vendor states this is by design and they do not consider it to be a security risk. 01/03/24 – ZDI informed the vendor that this is an expanded version of ZDI-CAN-20784, and they should reconsider their assessment of this case. 03/11/24 – The vendor states that their assessment of this case hasn’t changed. 08/05/24 – The ZDI informed the vendor that we are publishing this case as a zero-day advisory on 08/06/24. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2023-11-03 - Vulnerability reported to vendor
- 2024-08-06 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
