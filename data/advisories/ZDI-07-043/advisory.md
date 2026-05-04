# ZDI-07-043: Ipswitch IMail IMAP Daemon SUBSCRIBE Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-043
- **ZDI-CAN:** ZDI-CAN-179
- **Date:** 2007-07-19
- **CVE:** CVE-2007-2795
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Ipswitch
- **Affected Products:** IMail
- **Credit:** Sebastian Apelt (webmaster@buzzworld.org)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-043/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Ipswitch IMail and ICS server. Authentication is required to exploit this vulnerability. The specific flaw exists due to a lack of bounds checking during the parsing of arguments to the SUBSCRIBE IMAP command sent to the IMAP daemon listening by default on TCP port 143. By providing an overly long string as the argument, an exploitable stack-based buffer overflow occurs.

## Additional Details

Ipswitch has issued an update to correct this vulnerability. More details can be found at: http://www.ipswitch.com/support/imail/releases/im200621.asp

## Disclosure Timeline

- 2007-03-09 - Vulnerability reported to vendor
- 2007-07-19 - Coordinated public release of advisory
