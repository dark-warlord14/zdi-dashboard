# ZDI-08-025: Symantec Altiris Deployment Solution Domain Credential Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-025
- **ZDI-CAN:** ZDI-CAN-291
- **Date:** 2008-05-15
- **CVE:** CVE-2008-2291
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Altiris Deployment Solution
- **Credit:** Brett Moore of Insomnia Security www.insomniasec.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-025/
## Vulnerability Details

This vulnerability allows attackers to remotely obtain domain credentials on vulnerable installations of Symantec Altiris Deployment Solution. User interaction is not required to exploit this vulnerability. Authentication is not required to exploit this vulnerability. The specific flaw exists within the axengine.exe service listening by default on TCP port 402. The service allows a remote client to request encrypted domain credentials without authentication. The encryption lacks a salt allowing an attacker with a local installation of Altiris Deployment Solution to easily decrypt the credentials.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/avcenter/security/Content/2008.05.14a.html

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-05-15 - Coordinated public release of advisory
