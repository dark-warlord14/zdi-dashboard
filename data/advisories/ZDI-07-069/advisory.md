# ZDI-07-069: CA BrightStor ARCserve Backup Message Engine Insecure Method Exposure Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-069
- **ZDI-CAN:** ZDI-CAN-143
- **Date:** 2007-11-26
- **CVE:** CVE-2007-5328
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** BrightStor ARCserve Server
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-069/
## Vulnerability Details

This vulnerability allows attackers to arbitrarily access and modify the file system and registry of vulnerable installations of Computer Associates BrightStor ARCserve Backup. Authentication is not required to exploit this vulnerability. The specific flaws exists in the Message Engine RPC service which listens by default on TCP port 6504 with the following UUID: 506b1890-14c8-11d1-bbc3-00805fa6962e The service exposes a number of insecure method calls including: 0x17F, 0x180, 0x181, 0x182, 0x183, 0x184, 0x185, 0x186, 0x187, 0x188, 0x189, 0x18A, 0x18B, and 0x18C. Attackers can leverage these methods to manipulate both the file system and registry which can result in a complete system compromise.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: http://supportconnectw.ca.com/public/storage/infodocs/basb-secnotice.asp

## Disclosure Timeline

- 2007-01-12 - Vulnerability reported to vendor
- 2007-11-26 - Coordinated public release of advisory
