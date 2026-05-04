# ZDI-11-056: (0Day) Hewlett-Packard Data Protector Client EXEC_SETUP Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-056
- **ZDI-CAN:** ZDI-CAN-420
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0922
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-056/
## Vulnerability Details

This vulnerability allows an attacker to execute remote code on vulnerable installations of the Hewlett-Packard Data Protector client. User interaction is not required to exploit this vulnerability. The specific flaw exists within the implementation of the EXEC_SETUP command. This command instructs a Data Protector client to download and execute a setup file. A malicious attacker can instruct the client to access a file off of a share thus executing arbitrary code under the context of the current user.

## Disclosure Timeline

- 2009-01-26 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
