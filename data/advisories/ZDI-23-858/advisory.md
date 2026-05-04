# ZDI-23-858: (0Day) Pulse Secure Client SetupService Directory Traversal Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-858
- **ZDI-CAN:** ZDI-CAN-17687
- **Date:** 2023-06-14
- **CVE:** CVE-2023-34298
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Pulse Secure
- **Affected Products:** Client
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-858/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Pulse Secure Client. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within SetupService. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the service.

## Additional Details

07/08/22 – ZDI requested a vendor PSIRT contact. 07/13/22 – ZDI asked for an update. 07/26/22 – The vendor provided contact information. 07/27/22 – The ZDI reported the vulnerability to the vendor. 08/02/22 – The vendor acknowledged the report. 06/08/23 – The ZDI asked for an update and informed the vendor that the case will be published as a zero-day advisory on 06/14/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-07-27 - Vulnerability reported to vendor
- 2023-06-14 - Coordinated public release of advisory
