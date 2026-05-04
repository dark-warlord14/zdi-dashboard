# ZDI-14-117: Ecava IntegraXor Guest Acccount Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-117
- **ZDI-CAN:** ZDI-CAN-2041
- **Date:** 2014-05-02
- **CVE:** CVE-2014-0786
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Ecava
- **Affected Products:** IntegraXor
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-117/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Ecava IntegraXor. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the "guest" user. The issue lies in the ability the retrieve all project credentials. By abusing this flaw an attacker can disclose credentials and leverage this situation to achieve remote code execution.

## Additional Details

Ecava has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-091-01

## Disclosure Timeline

- 2013-12-18 - Vulnerability reported to vendor
- 2014-05-02 - Coordinated public release of advisory
