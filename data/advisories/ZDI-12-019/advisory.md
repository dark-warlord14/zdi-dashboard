# ZDI-12-019: IBM SPSS mraboutb.dll ActiveX Control SetLicenseInfoEx Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-019
- **ZDI-CAN:** ZDI-CAN-1295
- **Date:** 2012-01-30
- **CVE:** CVE-2012-0188
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** SPSS
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-019/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM SPSS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within SetLicenseInfoEx() method exposed by the mraboutb.dll ActiveX Control. String data supplied to the first parameter (strInstallDir) of SetLicenseInfoEx() is copied into a 256 byte global buffer without first checking the string length. This overflow can be exploited to remotely execute arbitrary code on the target system.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21577956

## Disclosure Timeline

- 2011-07-20 - Vulnerability reported to vendor
- 2012-01-30 - Coordinated public release of advisory
