# ZDI-15-575: Unitronics UniDownloader IPWorksSSL.HTTPS.1 ActiveX Control SSLCertHandle Property Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-575
- **ZDI-CAN:** ZDI-CAN-2930
- **Date:** 2015-12-02
- **CVE:** CVE-2015-7905
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Unitronics
- **Affected Products:** UniDownloader
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-575/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Unitronics UniDownloader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of the SSLCertHandle property of the IPWorksSSL.HTTPS ActiveX control. A crafted value can cause system software to treat arbitrary memory as a certificate structure which is then modified. An attacker can leverage this to attain remote code execution under the context of the user.

## Additional Details

Unitronics has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-274-02

## Disclosure Timeline

- 2015-05-20 - Vulnerability reported to vendor
- 2015-12-02 - Coordinated public release of advisory
