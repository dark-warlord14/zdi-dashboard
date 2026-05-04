# ZDI-23-1473: (0Day) Exim dnsdb Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1473
- **ZDI-CAN:** ZDI-CAN-17643
- **Date:** 2023-09-27
- **CVE:** CVE-2023-42119
- **CVSS:** 3.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Exim
- **Affected Products:** Exim
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1473/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Exim. Authentication is not required to exploit this vulnerability. The specific flaw exists within the smtp service, which listens on TCP port 25 by default. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

06/22/22 – ZDI reported the vulnerability to the vendor. 04/25/23 – ZDI asked for an update. 04/25/23 – The vendor asked us to re-send the reports. 05/10/23 – ZDI sent the vulnerability to the vendor. 09/25/23 – ZDI asked for an update and informed the vendor that we intend to publish the case as a zero-day advisory on 09/27/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-06-22 - Vulnerability reported to vendor
- 2023-09-27 - Coordinated public release of advisory
