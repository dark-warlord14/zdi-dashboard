# ZDI-15-574: Unitronics UniDownloader and Unitronics VisiLogic OPLC IDE IPWorksSSL.HTTPS.1 ActiveX Control WinSockPath Property Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-574
- **ZDI-CAN:** ZDI-CAN-2964
- **Date:** 2015-12-02
- **CVE:** CVE-2015-7905
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Unitronics, Unitronics
- **Affected Products:** UniDownloader VisiLogic OPLC IDE
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-574/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Unitronics UniDownloader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within implementation of the WinSockPath property of the HTTPS ActiveX control. The control passes this property as the URL for a DLL to the LoadLibraryA API, which will automatically execute DllMain in the DLL. This can be leveraged by an attacker for remote code execution in the context of the process.

## Additional Details

Unitronics has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-274-02 Unitronics has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-274-02

## Disclosure Timeline

- 2015-05-28 - Vulnerability reported to vendor
- 2015-12-02 - Coordinated public release of advisory
