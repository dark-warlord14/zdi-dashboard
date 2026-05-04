# ZDI-19-067: LAquis SCADA Web Server Hardcoded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-067
- **ZDI-CAN:** ZDI-CAN-6677
- **Date:** 2019-01-19
- **CVE:** CVE-2018-18998
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** LAquis SCADA
- **Affected Products:** Software
- **Credit:** Esteban Ruiz (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-067/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on vulnerable installations of LAquis SCADA Software. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of login requests to the product's webserver. The product contains a hard-coded password for a number of undocumented accounts. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

LAquis SCADA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-015-01

## Disclosure Timeline

- 2018-08-14 - Vulnerability reported to vendor
- 2019-01-19 - Coordinated public release of advisory
- 2019-01-19 - Advisory Updated
