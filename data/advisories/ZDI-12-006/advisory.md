# ZDI-12-006: Novell Netware XNFS.NLM NFS Rename Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-006
- **ZDI-CAN:** ZDI-CAN-1268
- **Date:** 2012-01-05
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Francis Provencher From Protek Research Lab's
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-006/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Netware. Authentication is not required to exploit this vulnerability. The flaw exists within the xnfs.nlm component which is used when handling NFS RPC requests. This process listens on UDP port 2049. When decoding the xdr encoded filename from an NFS_RENAME procedure request the process uses the user supplied length as the bounds for its copy to a stack buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the system.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=Cfw1tDezgbw~

## Disclosure Timeline

- 2011-06-03 - Vulnerability reported to vendor
- 2012-01-05 - Coordinated public release of advisory
