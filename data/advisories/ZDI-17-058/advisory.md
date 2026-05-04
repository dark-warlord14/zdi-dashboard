# ZDI-17-058: Ecava IntegraXor getdata name SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-058
- **ZDI-CAN:** ZDI-CAN-3849
- **Date:** 2017-02-07
- **CVE:** CVE-2016-8341
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Ecava
- **Affected Products:** IntegraXor
- **Credit:** Juan Pablo Lopez Yacubian
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-058/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Ecava IntegraXor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the name parameter in getdata requests. The issue lies in the failure to properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current process.

## Additional Details

Ecava has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-031-02

## Disclosure Timeline

- 2016-07-12 - Vulnerability reported to vendor
- 2017-02-07 - Coordinated public release of advisory
