# ZDI-11-090: Novell Netware RPC XNFS xdrDecodeString Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-090
- **ZDI-CAN:** ZDI-CAN-876
- **Date:** 2011-02-18
- **CVE:** CVE-2010-4227
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Francis Provencher for Protek Researchh Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-090/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Netware. Authentication is not required to exploit this vulnerability. The flaw exists within the XNFS.NLM component which listens by default on UDP port 1234. When handling the an NFS RPC request the xdrDecodeString function uses a user supplied length value to null terminate a string. This value can be signed allowing the NULL byte to be written at an arbitrary address. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the system.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=1z3z-OsVCiE~

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2011-02-18 - Coordinated public release of advisory
