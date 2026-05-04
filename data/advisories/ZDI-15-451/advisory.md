# ZDI-15-451: InduSoft Web Studio Remote Agent Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-451
- **ZDI-CAN:** ZDI-CAN-2649
- **Date:** 2015-09-28
- **CVE:** CVE-2015-7374
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Indusoft
- **Affected Products:** WebStudio
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-451/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of InduSoft WebStudio. User interaction is not required to exploit this vulnerability. The specific flaw exists within the Remote Agent service listening on TCP port 1234. The issue lies in the lack of authentication, allowing attackers to execute remote API calls on the service. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Indusoft has issued an update to correct this vulnerability. More details can be found at: http://www.schneider-electric.com/ww/en/download/document/SEVD-2015-251-01

## Disclosure Timeline

- 2015-02-06 - Vulnerability reported to vendor
- 2015-09-28 - Coordinated public release of advisory
