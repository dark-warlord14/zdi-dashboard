# ZDI-10-062: Novell Netware NWFTPD RMD/RNFR/DELE Argument Parsing Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-10-062
- **ZDI-CAN:** ZDI-CAN-383
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0625
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Nick DeBaggis Francis Provencher
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-062/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Netware NWFTPD daemon. Authentication or default anonymous access is required to exploit this vulnerability. The specific flaw exists when parsing malformed arguments to the verbs RMD, RNFR, and DELE. Overly long parameters will result in stack based buffer overflows which can be leveraged to execute arbitrary code.

## Additional Details

A public fix for this issue has been released in download nwftpd16.zip, available at http://download.novell.com/patch/finder/

## Disclosure Timeline

- 2008-08-26 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
