# ZDI-17-950: NetGain Enterprise Manager exec Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-950
- **ZDI-CAN:** ZDI-CAN-4749
- **Date:** 2017-12-13
- **CVE:** CVE-2017-16608
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** NetGain Systems
- **Affected Products:** Enterprise Manager
- **Credit:** Jacob Baines - Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-950/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Netgain Enterprise Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within exec.jsp. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

Fixed for NetGain Enterprise Manager - fixed version: v7.2.766 and above

## Disclosure Timeline

- 2017-07-05 - Vulnerability reported to vendor
- 2017-12-13 - Coordinated public release of advisory
