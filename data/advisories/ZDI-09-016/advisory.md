# ZDI-09-016: Novell Client/NetIdentity Agent Remote Arbitrary Pointer Dereference Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-016
- **ZDI-CAN:** ZDI-CAN-397
- **Date:** 2009-04-06
- **CVE:** CVE-2009-1350
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Ruben Santamarta
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-016/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Netware. A valid IPC$ connection must be established in order to exploit this vulnerability. The specific flaw exists within xtagent.exe during the handling of RPC messages over the XTIERRPCPIPE named pipe. Insufficient sanity checking allows remote attackers to dereference an arbitrary pointer which can be leveraged to execute code under the context of the system user.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=6ERQGPjRZ8o~

## Disclosure Timeline

- 2008-10-15 - Vulnerability reported to vendor
- 2009-04-06 - Coordinated public release of advisory
