# ZDI-14-251: Advantech WebAccess Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-251
- **ZDI-CAN:** ZDI-CAN-2086
- **Date:** 2014-07-18
- **CVE:** CVE-2014-2365
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** Advantech WebAccess
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-251/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the gmicons.asp functionality. By providing crafted requests, an attacker is able to delete or create arbitrary files as the WebAccess service. An attacker may leverage this to run arbitrary code in the context of the WebAccess service.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-198-02

## Disclosure Timeline

- 2014-04-23 - Vulnerability reported to vendor
- 2014-07-18 - Coordinated public release of advisory
