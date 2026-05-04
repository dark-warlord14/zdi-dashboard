# ZDI-11-256: Apple Quicktime Media Link src Parameter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-256
- **ZDI-CAN:** ZDI-CAN-1151
- **Date:** 2011-08-16
- **CVE:** CVE-2011-0248
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Chkr_d591
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-256/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime parses Quicktime Media Link (.qtl) files. The code which parses the .qtl parameter files fails to properly validate the size of the src parameter before copying it into a fixed length stack buffer. By supplying an overly long value for the src parameter, an attacker can leverage this flaw to execute malicious code within the context of the browser.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4826

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
