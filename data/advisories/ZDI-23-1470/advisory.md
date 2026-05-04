# ZDI-23-1470: (0Day) Exim SMTP Challenge Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1470
- **ZDI-CAN:** ZDI-CAN-17515
- **Date:** 2023-09-27
- **CVE:** CVE-2023-42116
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Exim
- **Affected Products:** Exim
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1470/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Exim. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of NTLM challenge requests. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

06/06/22 – ZDI requested a PSIRT contact. 06/14/22 – ZDI reported the vulnerability to the vendor. 04/25/23 – ZDI asked for an update. 04/25/23 – The vendor asked us to re-send the reports. 05/10/23 – ZDI sent the vulnerability to the vendor. 09/25/23 – ZDI asked for an update and informed the vendor that we intend to publish the case as a zero-day advisory on 09/27/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-06-14 - Vulnerability reported to vendor
- 2023-09-27 - Coordinated public release of advisory
