# ZDI-20-779: ICONICS Genesis64 TestQuery SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-779
- **ZDI-CAN:** ZDI-CAN-10288
- **Date:** 2020-06-30
- **CVE:** CVE-2020-12013
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ICONICS
- **Affected Products:** Genesis64
- **Credit:** Ben McBride
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-779/
## Vulnerability Details

The vulnerablity allows remote attackers to execute arbitrary code on affected installations of ICONICS Genesis64. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of requests to the TestQuery endpoint of the IcoFwxServer service. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

ICONICS has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-170-03

## Disclosure Timeline

- 2020-06-23 - Vulnerability reported to vendor
- 2020-06-30 - Coordinated public release of advisory
