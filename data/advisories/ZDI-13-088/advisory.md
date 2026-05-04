# ZDI-13-088: Novell ZENworks Mobile Management DUSAP.php Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-088
- **ZDI-CAN:** ZDI-CAN-1764
- **Date:** 2013-05-29
- **CVE:** CVE-2013-1082
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Novell
- **Affected Products:** ZENworks Mobile Management
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-088/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell ZENworks Mobile Management . Authentication is not required to exploit this vulnerability. The specific flaw exists within DUSAP.php, which receives a 'language' variable which later is used to include arbitrary resources from the local filesystem via require_once(). A remote attacker can abuse this to execute remote code under the context of the process running.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://www.novell.com/support/kb/doc.php?id=7011896

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
