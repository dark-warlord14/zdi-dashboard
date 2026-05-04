# ZDI-16-248: Trend Micro Mail Encryption Gateway SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-248
- **ZDI-CAN:** ZDI-CAN-3547
- **Date:** 2016-04-28
- **CVE:** CVE-2016-4351
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Trend Micro
- **Affected Products:** Email Encryption Gateway
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-248/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Email Encryption Gateway. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authentication functionality. The issue lies in the failure to sanitize user-supplied input prior to executing a SQL statement. An attacker could leverage this vulnerability to bypass authentication or execute code under the context of the database.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://esupport.trendmicro.com/solution/en-US/1114060.aspx

## Disclosure Timeline

- 2016-02-02 - Vulnerability reported to vendor
- 2016-04-28 - Coordinated public release of advisory
