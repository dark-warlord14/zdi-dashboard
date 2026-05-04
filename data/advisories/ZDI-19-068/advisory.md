# ZDI-19-068: LAquis SCADA Web Server URI Parsing Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-068
- **ZDI-CAN:** ZDI-CAN-7074
- **Date:** 2019-01-19
- **CVE:** CVE-2018-19000
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-068/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of LAquis SCADA Software. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of URIs by the product's web server. A crafted URI can cause the web service to bypass authentication that should be required for the web page. An attacker can leverage this vulnerability to access system information.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-015-01

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
- 2019-01-19 - Advisory Updated
