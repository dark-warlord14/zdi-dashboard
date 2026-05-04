# ZDI-16-240: Ecava IntegraXor Report batch SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-240
- **ZDI-CAN:** ZDI-CAN-3322
- **Date:** 2016-04-12
- **CVE:** CVE-2016-2299
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Ecava
- **Affected Products:** IntegraXor
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-240/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Ecava IntegraXor. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of batch report requests. The vulnerability is caused by the lack of input validation before using remotely supplied strings to construct SQL queries. By sending a specially crafted request to a vulnerable system, an unauthenticated remote attacker can exploit this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Ecava has produced a new release that addresses the reported vulnerabilities, as well as some identified security risks, in Version 5.0, build 4522. http://www.integraxor.com/download/beta.msi?5.0.4522.2 and https://ics-cert.us-cert.gov/advisories/ICSA-16-105-03

## Disclosure Timeline

- 2015-09-22 - Vulnerability reported to vendor
- 2016-04-12 - Coordinated public release of advisory
