# ZDI-23-1044: (0Day) Microsoft GitHub Dev-Containers Improper Privilege Management Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1044
- **ZDI-CAN:** ZDI-CAN-20784
- **Date:** 2023-08-08
- **CVE:** N/A
- **CVSS:** 9.9
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** GitHub
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1044/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Microsoft GitHub. Authentication is required to exploit this vulnerability. The specific flaw exists within the configuration of Dev-Containers. The application does not enforce the privileged flag within a devcontainer configuration. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the host.

## Additional Details

04/06/23 – ZDI reported the vulnerability to the vendor. 04/10/23 – The vendor asked us to resend the PoC. 04/19/23 – ZDI resent the PoC to the vendor. 05/16/23 – The vendor states this is by-design, and they do not consider it to be a security risk. 08/01/23 – ZDI provided the vendor with additional details on why this vulnerability should be remediated. 08/01/23 – The ZDI informed the vendor that the case is due on 08/04/23, and we will publish this case as a zero-day advisory on 08/08/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-04-06 - Vulnerability reported to vendor
- 2023-08-08 - Coordinated public release of advisory
- 2024-05-31 - Advisory Updated
