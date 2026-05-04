# ZDI-10-229: ProFTPD TELNET_IAC Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-229
- **ZDI-CAN:** ZDI-CAN-925
- **Date:** 2010-11-02
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ProFTPD
- **Affected Products:** FTP Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-229/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ProFTPD. Authentication is not required to exploit this vulnerability. The flaw exists within the proftpd server component which listens by default on TCP port 21. When reading user input if a TELNET_IAC escape sequence is encountered the process miscalculates a buffer length counter value allowing a user controlled copy of data to a stack buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the proftpd process.

## Additional Details

Patch committed to CVS with accompanying regression test, and backported to 1.3.3 branch. http://bugs.proftpd.org/show_bug.cgi?id=3521

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2010-11-02 - Coordinated public release of advisory
