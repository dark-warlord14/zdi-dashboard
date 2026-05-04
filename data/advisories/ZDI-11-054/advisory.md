# ZDI-11-054: (0Day) Hewlett-Packard Data Protector Client EXEC_CMD omni_chk_ds.sh Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-054
- **ZDI-CAN:** ZDI-CAN-418
- **Date:** 2011-02-07
- **CVE:** CVE-2011-0924
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-054/
## Vulnerability Details

This vulnerability allows an attacker to execute remote code on vulnerable installations of the Hewlett-Packard Data Protector client. User interaction is not required to exploit this vulnerability. The specific flaw exists within the filtering of the EXEC_CMD command. The Data Protector client only verifies file names, not their contents. By supplying malicious code within specific script files, arbitrary code execution is possible under the context of the current user.

## Disclosure Timeline

- 2009-01-26 - Vulnerability reported to vendor
- 2011-02-07 - Coordinated public release of advisory
