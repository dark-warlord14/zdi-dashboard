# ZDI-16-635: Fatek Automation Communication Server Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-635
- **ZDI-CAN:** ZDI-CAN-3681
- **Date:** 2016-12-14
- **CVE:** CVE-2016-5796
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Fatek Automation
- **Affected Products:** Communication Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-635/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fatek Automation Communication Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of query requests. An overly long string sent while querying a server can trigger a stack buffer overflow. An attacker can leverage this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Fatek Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-287-06

## Disclosure Timeline

- 2016-04-26 - Vulnerability reported to vendor
- 2016-12-14 - Coordinated public release of advisory
