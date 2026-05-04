# ZDI-10-139: Novell iPrint Client Browser Plugin Parameter Name Remote Code Execution

## Metadata

- **ZDI ID:** ZDI-10-139
- **ZDI-CAN:** ZDI-CAN-745
- **Date:** 2010-08-05
- **CVE:** CVE-2010-4314
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Novell
- **Affected Products:** iPrint
- **Credit:** Ivan Almuina
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-139/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Novell iPrint Client browser plugin. User interaction is required in that a target must visit a malicious web page. The specific flaw exists within handling plugin parameters. The application does not properly verify the name of parameters passed via <embed> tags. If a malicious attacker provides a long enough value a destination buffer can be overflowed. Successful exploitation leads to execution of arbitrary code under the context of the user owning the browser process.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=ftwZBxEFjIg~

## Disclosure Timeline

- 2010-06-02 - Vulnerability reported to vendor
- 2010-08-05 - Coordinated public release of advisory
