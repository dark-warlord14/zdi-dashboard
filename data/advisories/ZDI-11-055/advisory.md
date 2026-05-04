# ZDI-11-055: (0Day) Hewlett-Packard Data Protector Client EXEC_CMD Perl Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-055
- **ZDI-CAN:** ZDI-CAN-419
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0923
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-055/
## Vulnerability Details

This vulnerability allows an attacker to execute remote code on vulnerable installations of the Hewlett-Packard Data Protector client. User interaction is not required to exploit this vulnerability. The specific flaw exists within the filtering of arguments to the EXEC_CMD command. The Data Protector client allows remote connections to execute files within it's local bin directory. By supplying maliciously crafted input to the EXEC_CMD a remote attacker can interact with a Perl interpreter and execute arbitrary code under the context of the current user.

## Disclosure Timeline

- 2009-01-26 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
