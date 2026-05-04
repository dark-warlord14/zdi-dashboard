# ZDI-20-649: Eaton Intelligent Power Manager mc2 Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-649
- **ZDI-CAN:** ZDI-CAN-9854
- **Date:** 2020-05-12
- **CVE:** CVE-2020-6651
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Eaton
- **Affected Products:** Intelligent Power Manager
- **Credit:** Sivathmican Sivakumaran of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-649/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Eaton Intelligent Power Manager. Authentication is required to exploit this vulnerability. The specific flaw exists within system_srv.js. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root on Linux or SYSTEM on Windows.

## Additional Details

Eaton has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-133-01

## Disclosure Timeline

- 2019-12-23 - Vulnerability reported to vendor
- 2020-05-12 - Coordinated public release of advisory
