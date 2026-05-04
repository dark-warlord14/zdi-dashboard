# ZDI-14-249: Advantech WebAccess Remote Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-249
- **ZDI-CAN:** ZDI-CAN-2079
- **Date:** 2014-07-18
- **CVE:** CVE-2014-2367
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** Advantech WebAccess
- **Credit:** John Leitch
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-249/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication requirements on vulnerable installations of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ChkCookieNoRedir function. By providing arbitrary values to certain fields, an attacker can receive a session authentication cookie despite receiving an error message.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-198-02

## Disclosure Timeline

- 2014-04-23 - Vulnerability reported to vendor
- 2014-07-18 - Coordinated public release of advisory
