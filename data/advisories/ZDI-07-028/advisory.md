# ZDI-07-028: CA eTrust AntiVirus Server inoweb Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-028
- **ZDI-CAN:** ZDI-CAN-104
- **Date:** 2007-05-10
- **CVE:** CVE-2007-2522
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Computer Associates
- **Affected Products:** eTrust AntiVirus
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-028/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Computer Associates AntiVirus Server. User interaction is not required to exploit this vulnerability. The specific flaw exists in the authentication function of the inoweb service that listens by default on TCP port 12168. The function copies both the username and password into fixed-length stack buffers. If an attacker provides overly long values for these parameters, an exploitable buffer overflow occurs.

## Additional Details

Computer Associates has issued an update to correct this vulnerability. More details can be found at: http://supportconnectw.ca.com/public/antivirus/infodocs/caav-secnotice050807.asp

## Disclosure Timeline

- 2006-11-06 - Vulnerability reported to vendor
- 2007-05-10 - Coordinated public release of advisory
