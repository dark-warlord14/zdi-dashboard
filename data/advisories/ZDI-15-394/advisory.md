# ZDI-15-394: PHP Regular Expression Uninitialized Pointer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-394
- **ZDI-CAN:** ZDI-CAN-2547
- **Date:** 2015-08-17
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** PHP
- **Affected Products:** PHP
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-394/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of PHP. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of invalid regular expressions. The issue lies in the failure to properly initialize pointers in a buffer while executing a regular expression. An attacker can leverage this to disclose the contents of any address in memory in the context of the process running PHP.

## Additional Details

PHP has issued an update to correct this vulnerability. More details can be found at: http://vcs.pcre.org/pcre/code/trunk/pcre_exec.c?r1=1502&r2=1510

## Disclosure Timeline

- 2014-10-13 - Vulnerability reported to vendor
- 2015-08-17 - Coordinated public release of advisory
