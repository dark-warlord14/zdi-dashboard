# ZDI-25-088: mySCADA myPRO Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-088
- **ZDI-CAN:** ZDI-CAN-24784
- **Date:** 2025-02-19
- **CVE:** CVE-2025-20061
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** mySCADA
- **Affected Products:** myPRO
- **Credit:** Mehmet INCE (@mdisec) from PRODAFT.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-088/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of mySCADA myPRO. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web service, which listens on TCP port 34022 by default. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

mySCADA has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-25-023-01

## Disclosure Timeline

- 2024-09-13 - Vulnerability reported to vendor
- 2025-02-19 - Coordinated public release of advisory
- 2025-02-19 - Advisory Updated
