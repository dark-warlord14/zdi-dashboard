# ZDI-21-648: Advantech iView runProViewUpgrade Missing Authentication Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-648
- **ZDI-CAN:** ZDI-CAN-11832
- **Date:** 2021-06-07
- **CVE:** CVE-2021-32930
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** iView
- **Credit:** Selim Enes Karaduman (@Enesdex)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-648/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech iView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the runProViewUpgrade action of NetworkServlet, which listens on TCP port 8080 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to execute code in the context of the service acccount.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://us-cert.cisa.gov/ics/advisories/icsa-21-154-01

## Disclosure Timeline

- 2021-01-29 - Vulnerability reported to vendor
- 2021-06-07 - Coordinated public release of advisory
