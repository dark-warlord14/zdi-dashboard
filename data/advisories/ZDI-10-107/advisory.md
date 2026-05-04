# ZDI-10-107: Multiple Sourcefire Products Static Web SSL Keys Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-107
- **ZDI-CAN:** ZDI-CAN-799
- **Date:** 2010-06-10
- **CVE:** N/A
- **CVSS:** 7.7
- **CVSS Vector:** AV:A/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Sourcefire, Sourcefire, Sourcefire, Sourcefire
- **Affected Products:** 3D Sensor 1000 3D Sensor 2000 3D Sensor 9900 Defense Center 1000
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-107/
## Vulnerability Details

This vulnerability allows remote attackers to decrypt secure socket layer (SSL) communications directed to multiple Sourcefire products. The specific flaw exists within the reuse of private SSL keys for multiple devices and installations. The keypair is stored in /etc/ssl/server.crt and /etc/ssl/server.key. Disclosure of the private key allows an attacker to decrypt and monitor SSL communications with the target.

## Additional Details

Mitigation of this problem can be accomplished by replacing the static keys with custom keys. These instructions can be found in the installation guide for your product (available on the Sourcefire support site). https://support.sourcefire.com/notices/notice/1437

## Disclosure Timeline

- 2010-06-02 - Vulnerability reported to vendor
- 2010-06-10 - Coordinated public release of advisory
