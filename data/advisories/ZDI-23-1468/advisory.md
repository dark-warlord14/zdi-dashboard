# ZDI-23-1468: (0Day) Exim NTLM Challenge Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1468
- **ZDI-CAN:** ZDI-CAN-17433
- **Date:** 2023-09-27
- **CVE:** CVE-2023-42114
- **CVSS:** 3.7
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Exim
- **Affected Products:** Exim
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1468/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Exim. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of NTLM challenge requests. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to disclose information in the context of the service account.

## Additional Details

06/06/22 – ZDI requested a PSIRT contact. 06/14/22 – ZDI reported the vulnerability to the vendor. 04/25/23 – ZDI asked for an update. 04/25/23 – The vendor asked us to re-send the reports. 05/10/23 – ZDI sent the vulnerability to the vendor. 09/25/23 – ZDI asked for an update and informed the vendor that we intend to publish the case as a zero-day advisory on 09/27/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-06-14 - Vulnerability reported to vendor
- 2023-09-27 - Coordinated public release of advisory
